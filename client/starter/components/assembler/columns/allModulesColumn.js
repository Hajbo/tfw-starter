import React from "react";
import classNames from "classnames";
import styles from "./styles.module.css";

class AllModulesColumn extends React.Component {

  constructor(props) {
    console.log(props);
    super(props);
    this.state = {
      searchKeyword: null
    } 
    this.addModule = this.addModule.bind(this);
    this.setKeyword = this.setKeyword.bind(this);
    this.filterByKeyword = this.filterByKeyword.bind(this);
  }

  addModule(module) {
    this.props.onAddModule(module);
  }

  setKeyword(keyword) {
    this.setState({
      searchKeyword: keyword
    });
  }

  filterByKeyword(modules) {
    return this.state.searchKeyword
      ? modules.filter( module => module.name.toLowerCase().includes(this.state.searchKeyword.toLowerCase()))
      : modules
  }


  render() {
    return (
      <div className={styles["column-wrapper"] + ' ' + styles["module-column-all"]}>
        <div className={styles["column-header"]}>
          Available dependencies
          <br/>
          <input
            type="text"
            placeholder="Search by name"
            onChange={(e) => this.setKeyword(e.target.value)}
          />
        </div>
        <div className={styles["column-content"]}>
          {this.props.children
            ? this.filterByKeyword(this.props.children).map((module) => (
                <div className={styles.row + ' ' + styles["double-row"]} key={classNames(module.name, "item")}>
                  <div className={styles["row-header"]}>{module.name}<br/>{module.version}</div>
                  <button className={styles.btn}>
                    <i
                      className="fa fa-plus-circle"
                      onClick={(e) => this.addModule(module)}
                    ></i>
                  </button>
                </div>
              ))
            : <div className={styles.message}> Please select a framework </div>}
        </div>
      </div>
    );
  }
}

export default AllModulesColumn;

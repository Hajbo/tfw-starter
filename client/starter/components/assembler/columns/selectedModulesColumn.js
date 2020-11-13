import React from "react";
import classNames from "classnames";
import styles from "./styles.module.css";

class SelectedModulesColumn extends React.Component {
  constructor(props) {
    super(props);
    this.removeModule = this.removeModule.bind(this);
  }

  removeModule(module) {
    this.props.onRemoveModule(module);
  }

  render() {
    return (
      <div className={styles["module-column-selected"]}>
        {this.props.children
          ? this.props.children.map((module) => (
              <div className={styles.row} key={classNames(module.name, "item")}>
                <div className={styles["row-header"]}>{module.name}</div>
                <button className={styles.btn}>
                  {" "}
                  <i
                    className="fa fa-minus-circle"
                    onClick={(e) => this.removeModule(module)}
                  ></i>{" "}
                </button>
              </div>
            ))
          : "No framework was selected"}
      </div>
    );
  }
}

export default SelectedModulesColumn;

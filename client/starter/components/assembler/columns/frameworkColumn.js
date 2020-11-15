import React from "react";
import classNames from "classnames";
import styles from "./styles.module.css";

class FrameworkColumn extends React.Component {
  constructor(props) {
    super(props);
    this.handleSelect = this.handleSelect.bind(this);
  }

  handleSelect(event) {
    this.props.onFrameworkSelect(event.target.value);
  }

  render() {
    return (
      <div
        className={styles["column-wrapper"] + " " + styles["framework-column"]}
      >
        <div className={styles["column-header"]}>Frameworks</div>
        <div className={classNames(styles["column-content"], this.props.name)}>
          {this.props.children ? (
            this.props.children.map((framework) => (
              <div className={styles.row} key={classNames(framework, "item")}>
                <input
                  type="radio"
                  value={framework}
                  id={framework}
                  name={this.props.name}
                  onClick={this.handleSelect}
                />
                <label htmlFor={framework}>{framework}</label>
              </div>
            ))
          ) : (
            <div className={styles.message}> Please select a language </div>
          )}
        </div>
      </div>
    );
  }
}

export default FrameworkColumn;

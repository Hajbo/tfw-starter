import React from "react";
import classNames from "classnames";
import styles from "./styles.module.css";

class LanguageColumn extends React.Component {
  constructor(props) {
    super(props);
    this.handleSelect = this.handleSelect.bind(this);
  }

  handleSelect(event) {
    this.props.onLanguageSelect(event.target.value);
  }

  render() {
    return (
      <div className={styles["column-wrapper"] + ' ' + styles["language-column"]}>
        <div className={styles["column-header"]}>
          Languages
        </div>
        <div className={classNames(styles["column-content"], this.props.name)}>
          {this.props.children
            ? this.props.children.map((language) => (
                <div className={styles.row} key={classNames(language, "item")}>
                  <input
                    type="radio"
                    value={language}
                    id={language}
                    name={this.props.name}
                    onClick={this.handleSelect}
                  />
                  <label htmlFor={language}>{language}</label>
                </div>
              ))
            : <div className={styles.message}> Something went wrong 😨 </div>}
        </div>
      </div>
    );
  }
}

export default LanguageColumn;

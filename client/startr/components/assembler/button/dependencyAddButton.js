import React from "react";
import styles from "./styles.module.css";

class DependencyAddButton extends React.Component {
  constructor(props) {
    super(props);
    this.onClick = this.onClick.bind(this);
  }

  onClick() {
    this.props.onClick();
  }

  render() {
    return (
      <button
        className={
          styles["dependency-add-button"] + " " + styles["max-width-30"]
        }
        onClick={this.onClick}
        disabled={this.props.disabled}
      >
        Save
      </button>
    );
  }
}

export default DependencyAddButton;

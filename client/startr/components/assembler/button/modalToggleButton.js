import React from "react";
import styles from "./styles.module.css";

class ModalToggleButton extends React.Component {
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
        className={styles["dependency-add-button"]}
        onClick={this.onClick}
        disabled={this.props.disabled}
      >
        Add dependency
      </button>
    );
  }
}

export default ModalToggleButton;

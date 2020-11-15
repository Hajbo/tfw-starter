import React from "react";
import classNames from "classnames";
import Modal from "../modal";
import {ModalToggleButton} from "../button";
import styles from "./styles.module.css";

class SelectedModulesColumn extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isModalOpen: false
    };
    this.removeModule = this.removeModule.bind(this);
    this.toggleModal = this.toggleModal.bind(this);
    this.addExtraDependency = this.addExtraDependency.bind(this);
  }

  removeModule(module) {
    this.props.onRemoveModule(module);
  }

  toggleModal() {
    const { isModalOpen } = this.state;
    this.setState({ isModalOpen: !isModalOpen });
  }

  addExtraDependency(dependency) {
    console.log("SELECTMODULE");
    console.log(dependency);
    this.props.addExtraDependency(dependency);
  }

  render() {
    return (
      <div className={styles["column-wrapper"] + ' ' + styles["module-column-selected"]}>
        <div className={styles["column-header"]}>
          Selected dependencies
          <br/>
          <ModalToggleButton onClick={this.toggleModal} disabled={this.props.children ? false : true}/>
          <Modal isOpen={this.state.isModalOpen} onClose={this.toggleModal} onSave={this.addExtraDependency}/>
        </div>
        <div className={styles["column-content"]}>
          {this.props.children
            ? this.props.children.map((module) => (
                <div className={styles.row + ' ' + styles["double-row"]} key={classNames(module.name, "item")}>
                  <div className={styles["row-header"]}>{module.name}<br/>{module.version}</div>
                  <button className={styles.btn}>
                    <i
                      className="fa fa-minus-circle"
                      onClick={(e) => this.removeModule(module)}
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

export default SelectedModulesColumn;

import React from "react"
import styles from './styles.module.css'


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
            <div className={styles['module-column']}>
                {this.props.children ? this.props.children.map(module => <div onClick={e => this.removeModule(module)}>{module.name}</div>) : "No framework was selected"}
            </div>
        )
    }
}


export default SelectedModulesColumn;


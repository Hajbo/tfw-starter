import React from "react"
import styles from './styles.module.css'


class AllModulesColumn extends React.Component {

    constructor(props) {
        super(props);
        this.addModule = this.addModule.bind(this);
    }

    addModule(module) {
        this.props.onAddModule(module);
    }

    render() {
        return (
            <div className={styles['module-column']}>
                {this.props.children ? this.props.children.map(module => <div onClick={e => this.addModule(module)}>{module.name}</div>) : "No framework was selected"}
            </div>
        )
    }
}


export default AllModulesColumn;


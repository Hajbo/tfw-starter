import React from "react"
import classNames from "classnames"
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
            <div className={styles['module-column-all']}>
                {this.props.children ? this.props.children.map(module => 
                        <div className={styles.row} key={classNames(module.name, 'item')}>
                            <div className={styles['row-header']}>{module.name}</div>
                            <button className={styles.btn}> <i className="fa fa-plus-circle" onClick={e => this.addModule(module)}></i> </button> 
                        </div>) 
                        : "No framework was selected"
                }
            </div>
        )
    }
}


export default AllModulesColumn;


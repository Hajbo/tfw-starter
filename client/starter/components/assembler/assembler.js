import React from "react"
import {FrameworkColumn, LanguageColumn, AllModulesColumn, SelectedModulesColumn} from './columns'
import styles from './styles.module.css'


const test = [
    'A', 'B', 'C', 'D'
]

const selectedModules = [
    {'name': 'A'}
]

const allModules = [{'name': 'A'}, {'name': 'B'}, {'name': 'C'}, {'name': 'D'}]

class Assembler extends React.Component  {

    constructor(props) {
        super(props);
        this.state = {
            languages: {
                all: props.children,
                selected: null
            },
            frameworks: {
                all: null,
                selected: null
            },
            modules: {
                all: null,
                selected: null
            }
        };

        this.handleLanguageSelect = this.handleLanguageSelect.bind(this);
        this.handleFrameworkSelect = this.handleFrameworkSelect.bind(this);
        this.handleAddModule = this.handleAddModule.bind(this);
        this.handleRemoveModule = this.handleRemoveModule.bind(this);
    };

    handleLanguageSelect(selectedLanguage) {
        this.setState({
            languages: {
                all: this.state.languages.all,
                selected: selectedLanguage
            },
            frameworks: {
                all: test, // Some magic fetch
                selected: null
            },
            modules: this.state.modules
        })
    }

    handleFrameworkSelect(selectedFramework) {
        this.setState({
            languages: this.state.languages,
            frameworks: {
                all: this.state.frameworks.all,
                selected: selectedFramework
            },
            modules: {
                all: allModules.filter(module => !selectedModules.map(m => m.name).includes(module.name) ), // Some magic fetch
                selected: selectedModules // Some magic fetch
            }
        })
    }

    handleAddModule(toAdd) {
        console.log(toAdd);
        this.setState({
            languages: this.state.languages,
            frameworks: this.state.frameworks,
            modules: {
                all: this.state.modules.all.filter(existingModule => existingModule.name != toAdd.name),
                selected: this.state.modules.selected.concat(toAdd),
            }
        })
    }

    handleRemoveModule(toRemove) {
        this.setState({
            languages: this.state.languages,
            frameworks: this.state.frameworks,
            modules: {
                all: this.state.modules.all.concat([toRemove]),
                selected: this.state.modules.selected.filter(existingModule => existingModule.name != toRemove.name)
            }
        })
    }

    render() {
        return(
            <div className={styles.assembler}>
                <LanguageColumn 
                    children={this.state.languages.all} name='languages'
                    onLanguageSelect={this.handleLanguageSelect}    
                />
                <FrameworkColumn 
                    children={this.state.frameworks.all} name='frameworks'
                    onFrameworkSelect={this.handleFrameworkSelect}
                />
                <SelectedModulesColumn 
                    children={this.state.modules.selected}
                    onRemoveModule={this.handleRemoveModule}
                />
                <AllModulesColumn 
                    children={this.state.modules.all}
                    onAddModule={this.handleAddModule}
                />
            </div>
        )
    }
}


export default Assembler;
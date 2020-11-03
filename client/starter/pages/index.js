import Layout from "../components/layout"
import Assembler from "../components/assembler"

const Index = ({languages}) => <Layout> <Assembler >{languages}</Assembler> </Layout>;

Index.getInitialProps = async (ctx) => {
  //const res = await fetch('http://localhost:5000/api/v1/languages')
  //const json = await res.json()
  const json = {"supported_languages": ['Python', 'Node.js']}
  return { languages: json.supported_languages }
}

export default Index;
import Layout from "../components/layout"
import Assembler from "../components/assembler"

const Index = ({languages}) => <Layout> <Assembler languages={languages}></Assembler> </Layout>;

Index.getInitialProps = async (ctx) => {
  const res = await fetch('http://backend:5000/api/v1/languages')
  const json = await res.json()
  return { languages: json.supported_languages }
}

export default Index;
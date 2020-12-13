import Head from "next/head";
import Layout from "../components/layout";
import Assembler from "../components/assembler";

const Index = ({ languages }) => (
  <Layout>
    <Head>
      <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
      />
    </Head>
    <Assembler languages={languages}></Assembler>
  </Layout>
);

Index.getInitialProps = async (ctx) => {
  const res = await fetch("http://backend:5000/api/v1/languages");
  const json = await res.json();
  return { languages: json.supported_languages };
};

export default Index;

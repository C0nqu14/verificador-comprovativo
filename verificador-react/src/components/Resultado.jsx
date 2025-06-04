const Resultado = ({ data }) => {
    return (
      <div className="mt-8 bg-white p-6 rounded shadow-md max-w-4xl mx-auto">
        <h2 className="text-2xl font-bold mb-4">Resultado da Verificação</h2>
        <p><strong>Status:</strong> <span className="font-semibold">{data.status}</span></p>
        <p><strong>Confiabilidade:</strong> {data.score_confiabilidade}</p>
        <p><strong>OCR:</strong> {data.resultado_OCR}</p>
        <p><strong>Metadados:</strong> {data.resultado_metadados}</p>
        <p className="mt-4"><strong>Localização:</strong> {data.localizacao_ip?.cidade || '---'}, {data.localizacao_ip?.pais || '---'}</p>
  
        <div className="mt-4">
          <h3 className="font-semibold">Texto Extraído:</h3>
          <pre className="bg-gray-100 p-3 rounded overflow-x-auto">{data.texto_extraido}</pre>
        </div>
  
        <div className="mt-4">
          <h3 className="font-semibold">Metadados Brutos:</h3>
          <pre className="bg-gray-100 p-3 rounded overflow-x-auto">{JSON.stringify(data.metadados_extraidos, null, 2)}</pre>
        </div>
      </div>
    );
  };
  
  export default Resultado;

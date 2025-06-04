import UploadForm from './components/UploadForm';
import { useState } from 'react';
import Resultado from './components/Resultado';
import "./index.css"

function App() {
  const [resultado, setResultado] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center mb-6 text-blue-600">
        Jikulumesso
      </h1>
      <UploadForm onResult={setResultado} />
      {resultado && <Resultado data={resultado} />}
    </div>
  );
}

export default App;

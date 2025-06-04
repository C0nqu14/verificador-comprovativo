import { useState } from 'react';
import axios from 'axios';

const UploadForm = ({ onResult }) => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const enviar = async () => {
    if (!file) return alert("Escolha um comprovativo");

    const formData = new FormData();
    formData.append('ficheiro', file);

    try {
      setLoading(true);
      const res = await axios.post('http://localhost:5000/verificar', formData);
      {/*const res = await axios.post('https://verificador-comprovativo.onrender.com/verificar', formData);*/}
      onResult(res.data);
    } catch (err) {
      alert("Erro ao enviar");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white p-6 rounded shadow-md max-w-xl mx-auto">
      <input type="file" accept=".png,.jpg,.jpeg,.pdf" onChange={e => setFile(e.target.files[0])}/>
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded mt-4 hover:bg-blue-700"
        onClick={enviar}
        disabled={loading}
      >
        {loading ? "Analisando..." : "Verificar Comprovativo"}
      </button>
    </div>
  );
};

export default UploadForm;

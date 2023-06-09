import React, { useState } from 'react';
import '../InputForm.css';



const InputForm = () => {
  const [text, setText] = useState('');
  const [count, setCount] = useState(0);
  const [output, setOutput] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    setError('');

    if (!text && !count) {
      setError('Please enter both a string and a number.');
      return;
    }
    if(!text){
        setError('Please enter some text');
        return;
    }
    if(!count){
        setError('Please enter a number');
        return;
    }

    if (isNaN(count)) {
      setError('Please enter a valid number.');
      return;
    }

    setOutput(text.repeat(count));
  };

  return (
    <div className="input-form">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter a string"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <input
          type="number"
          placeholder="Enter a number"
          value={count}
          onChange={(e) => setCount(parseInt(e.target.value))}
        />
        <button type="submit">Submit</button>
      </form> 

      {error && <p className="error">{error}</p>}
      {output && <p>{output}</p>}
    </div>
  );
};

export default InputForm;

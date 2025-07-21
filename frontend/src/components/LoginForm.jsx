import { useState } from 'react';
import axios from 'axios';

function LoginForm({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:8000/api/token/', {username, password});
      localStorage.setItem('token', res.data.access);
      onLogin();
    } catch (err) {
      setError('Неверные данные');
    }
  };

  return (
    <div className="container">
      <form onSubmit={handleLogin}>
        <h2>Вход</h2>
        <input
          type="text"
          placeholder="Логин"
          value={username}
          onChange={e => setUsername(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Пароль"
          value={password}
          onChange={e => setPassword(e.target.value)}
          required
        />
        <button type="submit">Войти</button>
        {error && <p className="error-text">{error}</p>}
      </form>
    </div>
  );
}

export default LoginForm;

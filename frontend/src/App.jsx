import { useEffect, useState } from 'react';
import './App.css';
import TaskItem from './components/TaskItem';
import LoginForm from './components/LoginForm';
import api from './api';

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [loggedIn, setLoggedIn] = useState(!!localStorage.getItem('token'));

  const fetchTasks = () => {
    api.get('tasks/')
      .then(res => setTasks(res.data))
      .catch(err => {
        console.error('Ошибка загрузки: ', err);
        if (err.response?.status === 401) {
          setLoggedIn(false); 
        }
      });
  };

  useEffect(() => {
    if (loggedIn) {
      fetchTasks();
    }
  }, [loggedIn]);

  const handleSubmit = (e) => {
    e.preventDefault();
    api.post('tasks/', {
      title,
      description,
      status: 'pending',
      is_completed: false
    })
    .then(res => {
      setTasks([...tasks, res.data]);
      setTitle('');
      setDescription('');
    })
    .catch(err => console.error('Ошибка создания задачи: ', err));
  };

  const markCompleted = (id) => {
    api.patch(`tasks/${id}/`, { status: 'done' })
      .then(res => {
        setTasks(tasks.map(t => (t.id === id ? res.data : t)));
      });
  };

  const cancelTask = (id) => {
    api.patch(`tasks/${id}/`, { status: 'canceled' })
      .then(res => {
        setTasks(tasks.map(t => (t.id === id ? res.data : t)));
      });
  };

  const logout = () => {
    localStorage.removeItem('token');
    setLoggedIn(false);
  };

  if (!loggedIn) {
    return <LoginForm onLogin={() => setLoggedIn(true)} />;
  }

  return (
    <div className="container">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1>Task Tracker</h1>
        <button onClick={logout} style={{ background: '#e74c3c' }}>Выйти</button>
      </div>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Название задачи"
          value={title}
          onChange={e => setTitle(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Описание задачи"
          value={description}
          onChange={e => setDescription(e.target.value)}
        />
        <button type="submit">Добавить задачу</button>
      </form>

      <ul>
        {tasks.map(task => (
          <TaskItem
            key={task.id}
            task={task}
            onComplete={markCompleted}
            onCancel={cancelTask}
          />
        ))}
      </ul>
    </div>
  );
}

export default App;
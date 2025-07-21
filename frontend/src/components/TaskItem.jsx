import React from 'react';

function TaskItem({ task, onComplete, onCancel }) {
  const { id, title, description, status } = task;

  const statusLabels = {
  pending: 'В процессе',
  completed: 'Завершено',
  cancelled: 'Отменено',
};
  return (
    <li className="task-card">
        <h3>{title}</h3>
            <p>{description} — <span className={`status ${status}`}>{statusLabels[status] || status}</span></p>

            {status === 'pending' && (
                <div className="actions">
                <button onClick={() => onComplete(id)}>Завершить</button>
                <button className="cancel" onClick={() => onCancel(id)}>Отменить</button>
                </div>
            )
        }
    </li>
  );
}

export default TaskItem;
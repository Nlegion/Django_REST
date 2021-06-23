import React from 'react'

const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td>
                {project.id}
            </td>
            <td>
                {project.title}
            </td>
            <td>
                {project.user}
            </td>
            <td>
                {project.link}
            </td>
            <td>
                <button onClick={() => deleteProject(project.id)} type='submit'>Delete</button>
            </td>
        </tr>

    )
}

const ProjectList = ({projects, deleteProject}) => {
    return (
        <div>
            <table>
                <th>
                    ID
                </th>
                <th>
                    Имя проекта
                </th>
                <th>
                    Пользователи
                </th>
                <th>
                    ссылки
                </th>
                <th>
                    кнопка
                </th>
                {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}
            </table>
        </div>
    )
}

export default ProjectList;

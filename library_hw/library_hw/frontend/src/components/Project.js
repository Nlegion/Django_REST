import React from 'react'

const ProjectItem = ({project}) => {
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
        </tr>

    )
}

const ProjectList = ({projects}) => {
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
                {projects.map((project) => <ProjectItem project={project}/>)}
            </table>
        </div>
    )
}

export default ProjectList;
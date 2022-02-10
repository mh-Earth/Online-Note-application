import React from 'react'
import '../App.css';
function Note(props) {
    const requestOptions = {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
    };
    let url = "http://192.168.1.104:8000/api/note"
    let title = props.title.replaceAll(" ", "+");
    const deleteNote = () => {
        fetch(`${url}/${title}`,requestOptions).then((res)=>{})

        let note = document.getElementsByClassName("note")[props.index]
        note.style.display = "none"

    }
    return (



        <>
            <div className="note">
                <h2>{props.title}</h2>
                <p>{props.desc}</p>
                <div className="buttons">

                    <button onClick={deleteNote} >Delete</button>
                    {/* <button>Done</button> */}

                </div>
            </div>

            

        </>
    )
}

Note.defaultProps = {    
    desc:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum voluptatum voluptas error, nam perferendis quos nisi saepe eligendi iusto modi? Placeat ab ducimus nobis eius! Soluta dignissimos molestias voluptatibus modi?",
    title:"Lorem ipsum dolor sit amet consectetur adipisicing elit."

  }

export default Note

import React, { useState, useEffect } from 'react'
import Note from './Note'

export default function Main() {
  // form states
  const [note_title, setTitle] = useState("")
  const [note_desc, setnote_desc] = useState("")
  // form data state
  const [Notes, fetchNotes] = useState([])


  //  for adding note data to server
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: note_title, describe: note_desc })
  };
  let url = "http://192.168.1.104:8000/api/note"

  const addNote = async () => {
    await fetch(url, requestOptions).then((res) => {
      setTitle("")
      setnote_desc("")
    })
  }



  // states for form input hendeling
  const hendelCngTitle = (event) => {

    setTitle(event.target.value)


  }


  const hendelCngDesc = (event) => {

    setnote_desc(event.target.value)


  }
  //////////////////////////////////////////////////////
  //////////////////////////////////////////////////////


  const getnoteData = () => {
    // sending data to the server
    addNote().then(() => {

      // fetching the notes data from the server after add new note data
      fetch(url).then((res) => {

        return res.json();

      }).then((res) => {

        fetchNotes(res)


      }).catch(() => {

      })

    })
  }
  //////////////////////////////////////////////////////

  // fetching data for first time on commponet mount

  useEffect(() => {

    fetch(url).then((res) => {

      return res.json();

    }).then((res) => {

      fetchNotes(res)


    }).catch(() => {

    })

  }, [])
  ///////////////////////////////////////////////////////

  return (


    <>

      <main className='noteContainer'>



        {


          Notes.map((Element, index) => {

            return <Note key={Element.title} title={Element.title} desc={Element.describe} index={index} />


          })

        }



        <div className='form'>
          <p>Add a new note</p>

          <label htmlFor="title">Title</label>
          <input value={note_title} onChange={hendelCngTitle} type="text" name="title" id="title" />
          <label htmlFor="desc">Description</label>
          <textarea value={note_desc} onChange={hendelCngDesc} name="desc" id="" cols="20" rows="15"></textarea>
          <button onClick={getnoteData} disabled={note_desc === ""} >Add note</button>



        </div>



      </main>




    </>
  )
}

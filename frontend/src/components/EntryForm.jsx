import { useState } from "react";
import axios from "axios";

import MoodSelector from "./MoodSelector";
import EnergySlider from "./EnergySlider";

import "./../styles/entryform.css";

function EntryForm() {

    const [formData,setFormData]=useState({

        date:new Date().toISOString().split("T")[0],
        mood:"🙂",
        energy:5,
        win:"",
        song:"",
        expenses:[]

    });

    const [message,setMessage]=useState("");

    function handleChange(e){

        setFormData({
            ...formData,
            [e.target.name]:e.target.value
        });

    }

    async function handleSubmit(e){
        e.preventDefault();
        try{
            const response=await axios.post(
                "/entries/",
                formData
            );
            setMessage(response.data.msg);
        }

        catch(error){
            setMessage(
                error.response?.data?.detail ||
                "Something went wrong."
            );
        }
    }

    return(

        <form
            className="entry-form"
            onSubmit={handleSubmit}
        >

            <label>

                Date

                <input

                    type="date"

                    name="date"

                    value={formData.date}

                    onChange={handleChange}

                />

            </label>

            <label>

                Mood

                <MoodSelector

                    value={formData.mood}

                    onChange={(mood)=>

                        setFormData({

                            ...formData,

                            mood

                        })

                    }

                />

            </label>

            <EnergySlider

                value={formData.energy}

                onChange={(energy)=>

                    setFormData({

                        ...formData,

                        energy

                    })

                }

            />

            <label>

                Today's Win

                <textarea

                    name="win"

                    placeholder="What made today meaningful?"

                    value={formData.win}

                    onChange={handleChange}

                />

            </label>

            <label>

                Song of the Day

                <input

                    type="text"

                    name="song"

                    placeholder="Interstellar Theme..."

                    value={formData.song}

                    onChange={handleChange}

                />

            </label>

            <button
                className="submit-btn"
                type="submit"
            >

                Commit Aura

            </button>

            {

                message &&

                <p className="message">

                    {message}

                </p>

            }

        </form>

    );

}

export default EntryForm;
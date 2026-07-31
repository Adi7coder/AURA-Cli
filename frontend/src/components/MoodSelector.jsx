import "./../styles/entryform.css";

const moods = [
    "😔",
    "😕",
    "😐",
    "🙂",
    "😁",
    "LOCKEDIN 🤩"
];

function MoodSelector({ value, onChange }) {

    return (

        <div className="mood-grid">

            {moods.map((mood) => (

                <button
                    type="button"
                    key={mood}
                    className={
                        value === mood
                            ? "mood active"
                            : "mood"
                    }
                    onClick={() => onChange(mood)}
                >
                    {mood}
                </button>

            ))}

        </div>

    );

}

export default MoodSelector;
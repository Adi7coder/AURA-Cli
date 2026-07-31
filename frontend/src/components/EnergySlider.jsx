import "./../styles/entryform.css";

function EnergySlider({ value, onChange }) {

    return (

        <div>

            <div className="energy-top">

                <span>Energy</span>

                <strong>{value}/10</strong>

            </div>

            <input

                className="energy-slider"

                type="range"

                min="1"

                max="10"

                value={value}

                onChange={(e)=>onChange(e.target.value)}

            />

        </div>

    );

}

export default EnergySlider;
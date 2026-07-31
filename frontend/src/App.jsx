import "./styles/App.css";

import GlassCard from "./components/GlassCard";
import Header from "./components/Header";
import EntryForm from "./components/EntryForm";

function App() {
    return (
        <div className="app">

            <GlassCard>

                <Header />

                <EntryForm />

            </GlassCard>

        </div>
    );
}

export default App;
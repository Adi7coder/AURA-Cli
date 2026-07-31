import { Sparkles } from "lucide-react";
import { motion } from "framer-motion";

function Header() {

    return (

        <motion.div
            initial={{ opacity:0, y:-25 }}
            animate={{ opacity:1, y:0 }}
            transition={{ duration:.7 }}
            className="header"
        >

            <div className="logo">

                <Sparkles size={26} />

                <h1>Aura</h1>

            </div>

            <p>

                Capture today before it fades away.

            </p>

        </motion.div>

    );

}

export default Header;
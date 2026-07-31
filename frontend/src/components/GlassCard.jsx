import { motion } from "framer-motion";

function GlassCard({ children }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 35 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{
                duration: 0.7,
                ease: "easeOut"
            }}
            className="glass-card"
        >
            {children}
        </motion.div>
    );
}

export default GlassCard;

"use client";

import React, { useEffect, useRef, useState } from "react";

function Plot4_4() {
    const iframeRef = useRef(null);
    const [height, setHeight] = useState("0px");

    useEffect(() => {
        function handleMessage(event) {
            if (event.data?.type === "setHeight") {
                setHeight(`${event.data.height}px`);
            }
        }

        window.addEventListener("message", handleMessage);
        return () => window.removeEventListener("message", handleMessage);
    }, []);

    return (
        <iframe
            ref={iframeRef}
            src="/inr_gdp_inflation_stress_years.html"
            title="HTML Content"
            style={{
                border: "none",
                width: "100%",
                height,
                transition: "height 0.3s ease",
            }}
        />
    );
}

export default Plot4_4;


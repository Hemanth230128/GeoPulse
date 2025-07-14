
"use client";

import React, { useEffect, useRef, useState } from "react";

function Plot4_1() {
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
            src="/correlation_heatmap.html"
            title="HTML Content"
            style={{
                border: "none",
                width: "60%",
                height,
                transition: "height 0.3s ease",
                justify: "center",
            }}
        />
    );
}

export default Plot4_1;


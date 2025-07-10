"use client";

import React, { useEffect, useRef } from "react";
import vtkGenericRenderWindow from "vtk.js/Sources/Rendering/Misc/GenericRenderWindow";
import vtkHttpDataSetReader from "vtk.js/Sources/IO/Core/HttpDataSetReader";
import vtkVolumeMapper from "vtk.js/Sources/Rendering/Core/VolumeMapper";
import vtkVolume from "vtk.js/Sources/Rendering/Core/Volume";
import vtkColorTransferFunction from "vtk.js/Sources/Rendering/Core/ColorTransferFunction";
import vtkPiecewiseFunction from "vtk.js/Sources/Common/DataModel/PiecewiseFunction";

const PovertyVisualizer: React.FC = () => {
    const containerRef = useRef<HTMLDivElement | null>(null);

    useEffect(() => {
        if (!containerRef.current) return;

        const renderWindow = vtkGenericRenderWindow.newInstance();

        // Ensure DOM has rendered
        requestAnimationFrame(() => {
            const container = containerRef.current;
            if (!container) return;

            renderWindow.setContainer(container);
            renderWindow.resize();

            const renderer = renderWindow.getRenderer();
            const rw = renderWindow.getRenderWindow();

            const reader = vtkHttpDataSetReader.newInstance({ fetchGzip: false }) as any;
            reader.setUrl("/vtk/poverty_timeseries.vti");

            (reader.loadData() as Promise<void>)
                .then(() => {
                    const data = reader.getOutputData();

                    // 🚨 SAFETY CHECK
                    if (!data) {
                        console.error("VTK reader returned no data.");
                        return;
                    }

                    const mapper = vtkVolumeMapper.newInstance();
                    mapper.setSampleDistance(0.7);
                    mapper.setInputData(data);

                    const volume = vtkVolume.newInstance();
                    volume.setMapper(mapper);

                    const ctfun = vtkColorTransferFunction.newInstance();
                    ctfun.addRGBPoint(0.0, 0.1, 0.2, 0.8);
                    ctfun.addRGBPoint(0.5, 0.9, 0.8, 0.2);
                    ctfun.addRGBPoint(1.0, 0.8, 0.1, 0.1);

                    const ofun = vtkPiecewiseFunction.newInstance();
                    ofun.addPoint(0.0, 0.0);
                    ofun.addPoint(0.5, 0.3);
                    ofun.addPoint(1.0, 0.8);

                    const volProp = volume.getProperty();
                    volProp.setRGBTransferFunction(0, ctfun);
                    volProp.setScalarOpacity(0, ofun);
                    volProp.setShade(true);
                    volProp.setInterpolationTypeToFastLinear();
                    volProp.setAmbient(0.2);
                    volProp.setDiffuse(0.7);
                    volProp.setSpecular(0.3);
                    volProp.setSpecularPower(20.0);

                    renderer.addVolume(volume);
                    renderer.resetCamera();
                    rw.render();
                })
                .catch((err: any) => {
                    console.error("VTK load error:", err);
                });
        });
    }, []);

    return (
        <div
            ref={containerRef}
            style={{
                width: "100%",
                height: "600px",
                backgroundColor: "#000",
                borderRadius: "12px",
                overflow: "hidden",
            }}
        />
    );
};

export default PovertyVisualizer;

"use client";

import React, { useEffect, useState } from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";
import Papa from "papaparse";
import { scaleLinear } from "d3-scale";

// Define metrics from your CSV
type Metric =
    | "MPI Urban"
    | "Headcount Ratio Urban"
    | "Intensity of Deprivation Urban"
    | "MPI Rural"
    | "Headcount Ratio Rural"
    | "Intensity of Deprivation Rural";

interface CountryData {
    [key: string]: string;
}

const geoUrl =
    "https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson";

const WorldHeatmap: React.FC = () => {
    const [data, setData] = useState<CountryData[]>([]);
    const [selectedMetric, setSelectedMetric] = useState<Metric>("MPI Urban");
    const [isoHeaderKey, setIsoHeaderKey] = useState<string>("");

    useEffect(() => {
        Papa.parse<CountryData>("/MPI_national.csv", {
            download: true,
            header: true,
            complete: (results) => {
                console.log("📊 CSV Headers:", Object.keys(results.data[0]));
                console.log("📋 Sample CSV rows:", results.data.slice(0, 5));

                const key = Object.keys(results.data[0]).find((k) =>
                    k.toLowerCase().includes("iso")
                );
                if (key) {
                    setIsoHeaderKey(key);
                } else {
                    console.error("❌ ISO code column not found in CSV!");
                }

                setData(results.data);
            },
        });
    }, []);

    const metricDomains: Record<Metric, [number, number]> = {
        "MPI Urban": [0, 0.7],
        "MPI Rural": [0, 0.7],
        "Headcount Ratio Urban": [0, 100],
        "Headcount Ratio Rural": [0, 100],
        "Intensity of Deprivation Urban": [30, 60],
        "Intensity of Deprivation Rural": [30, 70],
    };

    const colorScale = scaleLinear<string>()
        .domain(metricDomains[selectedMetric])
        .range(["#ffe5e5", "#b30000"]);


    return (
        <div>
            <h2 className="text-xl font-bold text-center my-4">{selectedMetric} Heatmap</h2>

            <div className="text-center my-2">
                <label htmlFor="metric" className="mr-2">
                    Select Metric:
                </label>
                <select
                    id="metric"
                    value={selectedMetric}
                    onChange={(e) => setSelectedMetric(e.target.value as Metric)}
                    className="p-2 border rounded"
                >
                    <option value="MPI Urban">MPI Urban</option>
                    <option value="Headcount Ratio Urban">Headcount Ratio Urban</option>
                    <option value="Intensity of Deprivation Urban">Intensity of Deprivation Urban</option>
                    <option value="MPI Rural">MPI Rural</option>
                    <option value="Headcount Ratio Rural">Headcount Ratio Rural</option>
                    <option value="Intensity of Deprivation Rural">Intensity of Deprivation Rural</option>
                </select>
            </div>

            <ComposableMap projectionConfig={{ scale: 160 }}>
                <Geographies geography={geoUrl}>
                    {({ geographies }) =>
                        geographies.map((geo) => {
                            const props = geo.properties;
                            const iso = props["ISO3166-1-Alpha-3"];

                            console.log("🌍 Geo properties:", props);

                            let countryDatum: CountryData | undefined = undefined;
                            if (isoHeaderKey) {
                                countryDatum = data.find(
                                    (d) => d[isoHeaderKey]?.trim().toUpperCase() === iso
                                );
                            }

                            const raw = countryDatum?.[selectedMetric];
                            const value =
                                typeof raw === "string" ? parseFloat(raw.trim()) : undefined;

                            console.log(
                                `✅ Matching ISO: ${iso} | Match: ${countryDatum?.Country || "undefined"
                                }`
                            );
                            console.log(`📈 Metric: ${selectedMetric} | Raw: "${raw}" | Value: ${value}`);

                            return (
                                <Geography
                                    key={geo.rsmKey}
                                    geography={geo}
                                    fill={
                                        typeof value === "number" && !isNaN(value)
                                            ? colorScale(value)
                                            : "#EEE"
                                    }
                                    stroke="#FFF"
                                />
                            );
                        })
                    }
                </Geographies>
            </ComposableMap>
        </div>
    );
};

export default WorldHeatmap;

export const sections = [
  {
    id: '1',
    title: 'Population Density vs Poverty Index',
    description: "High population density doesn't always equate to poverty - distribution is uneven and often misunderstood.",
    aiHint: 'population poverty',
    href: '/section/1',
    imgSrc: 'https://placehold.co/600x400/9DB17C/FFFFFF.png',
    subsections: [
      { id: 'a', name: 'MPI Comparison' },
      { id: 'b', name: 'Trend Filtering' },
      { id: 'c', name: 'Mismatched Regions' },
      { id: 'd', name: 'Interactive World Map' },
      { id: 'e', name: 'Visualization Types' },
    ],
  },
  {
    id: '2',
    title: 'Malnutrition vs GDP, Literacy, Sanitation',
    description: "Economic growth alone doesn't eliminate malnutrition - education and basic services are key drivers.",
    aiHint: 'malnutrition chart',
    href: '/section/2',
    imgSrc: 'https://placehold.co/600x400/A9B4C2/FFFFFF.png',
    subsections: [
        { id: 'a', name: 'Indicator Correlation' },
        { id: 'b', name: 'Highlight Malnutrition' },
        { id: 'c', name: 'Granular Segmentation' },
        { id: 'd', name: 'Chart Visualizations' },
    ],
  },
  {
    id: '3',
    title: 'Urbanization, Migration, Brain Drain',
    description: 'Rapid urbanization and limited opportunities drive internal migration and international brain drain.',
    aiHint: 'urbanization migration',
    href: '/section/3',
    imgSrc: 'https://placehold.co/600x400/C7B8A9/FFFFFF.png',
    subsections: [
        { id: 'a', name: 'Migration Analysis' },
        { id: 'b', name: 'Skill Shortage Identification' },
        { id: 'c', name: 'Push/Pull Factor Comparison' },
        { id: 'd', name: 'Dynamic Storytelling Charts' },
    ],
  },
  {
    id: '4',
    title: 'INR Depreciation and Macroeconomic Indicators',
    description: 'Currency value is affected by macro factors like inflation, trade balance, and population pressure.',
    aiHint: 'currency chart',
    href: '/section/4',
    imgSrc: 'https://placehold.co/600x400/BDB7AB/FFFFFF.png',
    subsections: [
        { id: 'a', name: 'INR/USD Trend Visualization' },
        { id: 'b', name: 'Regional Currency Comparison' },
        { id: 'c', name: 'Economic Stress Correlation' },
        { id: 'd', name: 'Trend Exploration Charts' },
    ],
  },
  {
    id: '5',
    title: 'Predictive Risk Mapping',
    description: 'Some Indian regions may face future risks in poverty or malnutrition due to current demographic trends.',
    aiHint: 'risk map',
    href: '/section/5',
    imgSrc: 'https://placehold.co/600x400/DDCDBE/FFFFFF.png',
    subsections: [
        { id: 'a', name: 'Composite Risk Score' },
        { id: 'b', name: '2030 Risk Zone Forecast' },
        { id: 'c', name: 'Interactive Heatmaps' },
        { id: 'd', name: 'Granular Policy Targeting' },
    ],
  },
];

export function getSectionData(sectionId: string) {
    return sections.find(section => section.id === sectionId);
}

export function getSubsectionData(sectionId: string, subsectionId: string) {
    const section = getSectionData(sectionId);
    if (!section) return undefined;
    return section.subsections.find(subsection => subsection.id === subsectionId);
}

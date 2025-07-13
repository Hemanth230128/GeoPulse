import {
  AreaChart,
  HeartPulse,
  ArrowRightLeft,
  TrendingUp,
  Map,
} from 'lucide-react';

export const sections = [
  {
    id: '1',
    title: 'Population\nDensity vs.\nPoverty',
    href: '/section/1',
    Icon: AreaChart,
    subsections: [
      {
        id: 'a',
        name: 'Compare population density with Multidimensional Poverty Index (MPI) at global and regional levels.',
      },
      {
        id: 'b',
        name: 'Filter by year and income group to analyze trends across time and economies.',
      },
      {
        id: 'c',
        name: 'Identify mismatched regions (e.g., low-density high-poverty zones) for targeted development.',
      },
      {
        id: 'd',
        name: 'Build an interactive world map with focus-and-context mechanics to highlight poverty-density mismatches.',
      },
      {
        id: 'e',
        name: 'Use choropleth maps, scatter plots, and bivariate grids for intuitive comparison.',
      },
    ],
  },
  {
    id: '2',
    title: 'Malnutrition\n& Development',
    href: '/section/2',
    Icon: HeartPulse,
    subsections: [
      {
        id: 'a',
        name: 'Correlate malnutrition rates with GDP per capita, female literacy, and sanitation access.',
      },
      {
        id: 'b',
        name: 'Highlight regions where malnutrition remains high despite economic progress.',
      },
      {
        id: 'c',
        name: 'Segment by year, region, and child population density for granular insights.',
      },
      {
        id: 'd',
        name: 'Use bubble charts, stacked bar plots, and population pyramids to visualize relationships.',
      },
    ],
  },
  {
    id: '3',
    title: 'Urbanization\n& Migration',
    href: '/section/3',
    Icon: ArrowRightLeft,
    subsections: [
      {
        id: 'a',
        name: 'Analyze urbanization rates alongside net migration and emigration patterns.',
      },
      {
        id: 'b',
        name: 'Identify countries/regions facing skill shortages due to brain drain.',
      },
      {
        id: 'c',
        name: 'Compare migration push/pull factors such as education levels and unemployment.',
      },
      {
        id: 'd',
        name: 'Use flow maps, Sankey diagrams, and animated line charts for dynamic storytelling.',
      },
    ],
  },
  {
    id: '4',
    title: 'INR\nDepreciation',
    href: '/section/4',
    Icon: TrendingUp,
    subsections: [
      {
        id: 'a',
        name: 'Visualize INR/USD trends alongside GDP growth, inflation, and demographic changes.',
      },
      {
        id: 'b',
        name: "Compare India's currency trends with other South Asian economies.",
      },
      {
        id: 'c',
        name: 'Explore how economic stress correlates with currency depreciation phases.',
      },
      {
        id: 'd',
        name: 'Use multi-line time series, correlation heatmaps, and area charts for trend exploration.',
      },
    ],
  },
  {
    id: '5',
    title: 'Predictive\nRisk Map',
    href: '/section/5',
    Icon: Map,
    subsections: [
      {
        id: 'a',
        name: 'Create a composite risk score using child population growth, literacy, and sanitation access.',
      },
      {
        id: 'b',
        name: 'Forecast 2030 risk zones across Indian states and districts.',
      },
      {
        id: 'c',
        name: 'Display results as interactive heatmaps and filters for planning interventions.',
      },
      {
        id: 'd',
        name: 'Use choropleth layers, interactive dashboards, and range sliders to support granular policy targeting.',
      },
    ],
  },
];

export function getSectionData(sectionId) {
  const section = sections.find((section) => section.id === sectionId);
  if (section) {
    // Return a version of the section with the title formatted for display outside the homepage cards
    return {
      ...section,
      title: section.title.replace(/\n/g, ' '),
    };
  }
  return undefined;
}

export function getSubsectionData(sectionId, subsectionId) {
  const section = sections.find((section) => section.id === sectionId);
  if (!section) return undefined;
  return section.subsections.find(
    (subsection) => subsection.id === subsectionId
  );
}

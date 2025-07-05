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
    title: 'Population Density vs. Poverty',
    description:
      'Compare MPI, filter trends, and explore regions on an interactive map.',
    href: '/section/1',
    Icon: AreaChart,
    subsections: [
      { id: 'a', name: 'MPI Comparison' },
      { id: 'b', name: 'Trend Filtering' },
      { id: 'c', name: 'Mismatched Regions' },
    ],
  },
  {
    id: '2',
    title: 'Malnutrition & Development',
    description:
      'Correlate indicators, highlight malnutrition, and segment data with various charts.',
    href: '/section/2',
    Icon: HeartPulse,
    subsections: [
      { id: 'a', name: 'Indicator Correlation' },
      { id: 'b', name: 'Highlight Malnutrition' },
      { id: 'c', name: 'Granular Segmentation' },
    ],
  },
  {
    id: '3',
    title: 'Urbanization & Migration',
    description:
      'Analyze migration, identify skill shortages, and compare push/pull factors.',
    href: '/section/3',
    Icon: ArrowRightLeft,
    subsections: [
      { id: 'a', name: 'Migration Analysis' },
      { id: 'b', name: 'Skill Shortage Identification' },
      { id: 'c', name: 'Push/Pull Factor Comparison' },
    ],
  },
  {
    id: '4',
    title: 'INR Depreciation',
    description:
      'Visualize currency trends, compare regional data, and correlate with economic stress.',
    href: '/section/4',
    Icon: TrendingUp,
    subsections: [
      { id: 'a', name: 'INR/USD Trend Visualization' },
      { id: 'b', name: 'Regional Currency Comparison' },
      { id: 'c', name: 'Economic Stress Correlation' },
    ],
  },
  {
    id: '5',
    title: 'Predictive Risk Map',
    description:
      'Calculate composite risk, forecast future risk zones, and target policy with heatmaps.',
    href: '/section/5',
    Icon: Map,
    subsections: [
      { id: 'a', name: 'Composite Risk Score' },
      { id: 'b', name: '2030 Risk Zone Forecast' },
      { id: 'c', name: 'Interactive Heatmaps' },
    ],
  },
];

export function getSectionData(sectionId) {
  return sections.find((section) => section.id === sectionId);
}

export function getSubsectionData(sectionId, subsectionId) {
  const section = getSectionData(sectionId);
  if (!section) return undefined;
  return section.subsections.find(
    (subsection) => subsection.id === subsectionId
  );
}

import type { LucideIcon } from 'lucide-react';
import {
  AreaChart,
  HeartPulse,
  ArrowRightLeft,
  TrendingUp,
  Map,
} from 'lucide-react';

export type Section = {
  id: string;
  title: string;
  description: string;
  href: string;
  Icon: LucideIcon;
  subsections: {
    id: string;
    name: string;
  }[];
};

export const sections: Section[] = [
  {
    id: '1',
    title: 'Visualization Task 1',
    description:
      'Analyze the relationship between Population Density and the Poverty Index.',
    href: '/section/1',
    Icon: AreaChart,
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
    title: 'Visualization Task 2',
    description:
      'Explore the correlation between Malnutrition and key development indicators.',
    href: '/section/2',
    Icon: HeartPulse,
    subsections: [
      { id: 'a', name: 'Indicator Correlation' },
      { id: 'b', name: 'Highlight Malnutrition' },
      { id: 'c', name: 'Granular Segmentation' },
      { id: 'd', name: 'Chart Visualizations' },
    ],
  },
  {
    id: '3',
    title: 'Visualization Task 3',
    description:
      'Investigate the impact of Urbanization, Migration, and Brain Drain.',
    href: '/section/3',
    Icon: ArrowRightLeft,
    subsections: [
      { id: 'a', name: 'Migration Analysis' },
      { id: 'b', name: 'Skill Shortage Identification' },
      { id: 'c', name: 'Push/Pull Factor Comparison' },
      { id: 'd', name: 'Dynamic Storytelling Charts' },
    ],
  },
  {
    id: '4',
    title: 'Visualization Task 4',
    description:
      'Track the relationship between INR Depreciation and Macroeconomic Indicators.',
    href: '/section/4',
    Icon: TrendingUp,
    subsections: [
      { id: 'a', name: 'INR/USD Trend Visualization' },
      { id: 'b', name: 'Regional Currency Comparison' },
      { id: 'c', name: 'Economic Stress Correlation' },
      { id: 'd', name: 'Trend Exploration Charts' },
    ],
  },
  {
    id: '5',
    title: 'Visualization Task 5',
    description:
      'Develop a Predictive Risk Map for key socio-economic challenges.',
    href: '/section/5',
    Icon: Map,
    subsections: [
      { id: 'a', name: 'Composite Risk Score' },
      { id: 'b', name: '2030 Risk Zone Forecast' },
      { id: 'c', name: 'Interactive Heatmaps' },
      { id: 'd', name: 'Granular Policy Targeting' },
    ],
  },
];

export function getSectionData(sectionId: string) {
  return sections.find((section) => section.id === sectionId);
}

export function getSubsectionData(sectionId: string, subsectionId: string) {
  const section = getSectionData(sectionId);
  if (!section) return undefined;
  return section.subsections.find(
    (subsection) => subsection.id === subsectionId
  );
}
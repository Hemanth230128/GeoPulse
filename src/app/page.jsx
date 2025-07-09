import Link from 'next/link';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { AreaChart, HeartPulse, ArrowLeftRight, TrendingUp, Map } from 'lucide-react';

const sections = [
  {
    title: 'Population Density vs. Poverty',
    href: '/population-density-vs-poverty',
    description: 'Compare MPI, filter trends, and explore regions on an interactive map.',
    icon: <AreaChart className="w-14 h-14 text-primary/30 group-hover:text-primary transition-colors duration-300" />,
  },
  {
    title: 'Malnutrition & Development',
    href: '/malnutrition-development',
    description: 'Correlate indicators, highlight malnutrition, and segment data with various charts.',
    icon: <HeartPulse className="w-14 h-14 text-primary/30 group-hover:text-primary transition-colors duration-300" />,
  },
  {
    title: 'Urbanization & Migration',
    href: '/urbanization-migration',
    description: 'Analyze migration, identify skill shortages, and compare push/pull factors.',
    icon: <ArrowLeftRight className="w-14 h-14 text-primary/30 group-hover:text-primary transition-colors duration-300" />,
  },
  {
    title: 'INR Depreciation',
    href: '/inr-depreciation',
    description: 'Visualize currency trends, compare regional data, and correlate with economic stress.',
    icon: <TrendingUp className="w-14 h-14 text-primary/30 group-hover:text-primary transition-colors duration-300" />,
  },
  {
    title: 'Predictive Risk Map',
    href: '/predictive-risk-map',
    description: 'Calculate composite risk, forecast future risk zones, and target policy with heatmaps.',
    icon: <Map className="w-14 h-14 text-primary/30 group-hover:text-primary transition-colors duration-300" />,
  },
];

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center text-center py-12 sm:py-20">
      <div className="container px-4 md:px-6">
        <div className="max-w-3xl mx-auto mb-8 -translate-y-4">
          <h1 className="text-5xl font-bold tracking-tight sm:text-6xl text-foreground -mb-1">
            GeoPulse
          </h1>
          <p className="mt-4 text-lg text-muted-foreground md:text-xl">
            Actionable insights on impulse, feel the world's true pulse.
          </p>
        </div>
        <div className="max-w-7xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6">
          {sections.map((section) => (
            <Link
              href={section.href}
              key={section.href}
              className="flex"
            >
              <Card className="w-full text-left shadow-md hover:shadow-lg transition-all duration-500 ease-in-out hover:-translate-y-1 flex flex-col group p-4 h-[26rem]">
                <div className="flex-grow">
                  <CardHeader className="p-0 mb-2">
                    <CardTitle className="font-bold text-2xl leading-tight text-primary">{section.title}</CardTitle>
                  </CardHeader>
                  <CardContent className="p-0">
                    <p className="text-muted-foreground text-sm">{section.description}</p>
                  </CardContent>
                </div>
                <div className="flex-shrink-0 pt-4 flex justify-center items-center">
                  {section.icon}
                </div>
              </Card>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
}

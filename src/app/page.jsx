import Link from 'next/link';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { AreaChart, HeartPulse, ArrowLeftRight, TrendingUp, Map } from 'lucide-react';

const sections = [
  {
    title: 'Population Density vs. Poverty',
    href: '/population-density-vs-poverty',
    description: 'Compare MPI, filter trends, and explore regions on an interactive map.',
    icon: <AreaChart className="w-10 h-10 text-muted-foreground group-hover:text-primary transition-colors" />,
  },
  {
    title: 'Malnutrition & Development',
    href: '/malnutrition-development',
    description: 'Correlate indicators, highlight malnutrition, and segment data with various charts.',
    icon: <HeartPulse className="w-10 h-10 text-muted-foreground group-hover:text-primary transition-colors" />,
  },
  {
    title: 'Urbanization & Migration',
    href: '/urbanization-migration',
    description: 'Analyze migration, identify skill shortages, and compare push/pull factors.',
    icon: <ArrowLeftRight className="w-10 h-10 text-muted-foreground group-hover:text-primary transition-colors" />,
  },
  {
    title: 'INR Depreciation',
    href: '/inr-depreciation',
    description: 'Visualize currency trends, compare regional data, and correlate with economic stress.',
    icon: <TrendingUp className="w-10 h-10 text-muted-foreground group-hover:text-primary transition-colors" />,
  },
  {
    title: 'Predictive Risk Map',
    href: '/predictive-risk-map',
    description: 'Calculate composite risk, forecast future risk zones, and target policy with heatmaps.',
    icon: <Map className="w-10 h-10 text-muted-foreground group-hover:text-primary transition-colors" />,
  },
];

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center text-center py-16 sm:py-24">
      <div className="container px-4 md:px-6">
        <div className="max-w-3xl mx-auto mb-12">
          <h1 className="text-5xl font-bold tracking-tight sm:text-6xl text-foreground">
            GeoPulse
          </h1>
          <p className="mt-4 text-lg text-muted-foreground md:text-xl">
            Actionable insights on impulse, feel the world's true pulse.
          </p>
        </div>
        <div className="max-w-6xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6">
          {sections.map((section) => (
            <Link
              href={section.href}
              key={section.href}
              className="flex"
            >
              <Card className="w-full text-left shadow-md hover:shadow-lg transition-all duration-300 ease-in-out hover:-translate-y-1 flex flex-col group p-4 h-64">
                <div className="flex-grow">
                  <CardHeader className="p-0 mb-2">
                    <CardTitle className="font-bold text-base leading-tight text-primary">{section.title}</CardTitle>
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

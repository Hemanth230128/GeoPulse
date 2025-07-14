import { notFound } from 'next/navigation';
import Link from 'next/link';
import { navConfig } from '@/config/nav';
import { Card, CardContent } from '@/components/ui/card';
import { Home, ChevronRight } from 'lucide-react';
import Plot1_1 from '@/components/1.1plot';
import Plot1_2 from '@/components/1.2plot';
import Plot2_1 from '@/components/2.1plot';
import Plot2_2 from '@/components/2.2plot';
import Plot3_1 from '@/components/3.1plot';
import Plot3_2 from '@/components/3.2plot';
import Plot4_1 from '@/components/4.1plot';
import Plot4_2 from '@/components/4.2plot';
import Plot4_3 from '@/components/4.3plot';
import Plot4_4 from '@/components/4.4plot';

function unslugify(slug) {
  return slug.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

export default function SubsectionPage({ params }) {
  const { section, subsection } = params;
  const navSection = navConfig.sidebarNav[section];

  if (!navSection || !navSection.find(item => item.href === `/${section}/${subsection}`)) {
    notFound();
  }

  const title = unslugify(subsection);
  const sectionTitle = unslugify(section);

  return (
    <div className="animate-fade-in">
      <div className="flex items-center space-x-2 text-sm text-muted-foreground mb-4">
        <Link href="/" className="hover:text-foreground">
          <Home className="h-4 w-4" />
        </Link>
        <ChevronRight className="h-4 w-4" />
        <Link href={`/${section}`} className="hover:text-foreground">{sectionTitle}</Link>
        <ChevronRight className="h-4 w-4" />
        <span className="font-medium text-foreground">{title}</span>
      </div>
      <Card className="shadow-lg">
        <CardContent className="p-6">
          <h1 className="text-3xl font-bold text-center mb-3">{title}</h1>
          {(section === "poverty-patterns" && subsection === "low-vs-high-mpi-regions") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot1_1 />
            </div>
          )}
          {(section === "poverty-patterns" && subsection === "population-density-vs-mpi") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot1_2 />
            </div>
          )}
          {(section === "growth-vs-development" && subsection === "malnutrition-vs-gdp-growth") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot2_1 />
            </div>
          )}
          {(section === "growth-vs-development" && subsection === "tracking-progress") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot2_2 />
            </div>
          )}
          {(section === "urban-growth-and-migration-trends" && subsection === "urban-drift") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot3_1 />
            </div>
          )}
          {(section === "urban-growth-and-migration-trends" && subsection === "global-miigration-flow-by-continent") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot3_2 />
            </div>
          )}
          {(section === "economic-forces-and-currency-depreciation" && subsection === "economic-echoes") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden flex justify-center">
              <Plot4_1 />
            </div>
          )}
          {(section === "economic-forces-and-currency-depreciation" && subsection === "depreciation-spread") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot4_2 />
            </div>
          )}
          {(section === "economic-forces-and-currency-depreciation" && subsection === "south-asian-currency-trends") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot4_3 />
            </div>
          )}
          {(section === "economic-forces-and-currency-depreciation" && subsection === "indian-economic-trio") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot4_4 />
            </div>
          )}
          {(section === "indian-risk-map-forecast" && subsection === "risk-spotlight") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <div style={{ width: '100%', height: '800px', margin: '2rem 0' }}>
                <iframe
                  src="https://geopulse-dash-backend.up.railway.app/"
                  title="Dash App"
                  width="100%"
                  height="100%"
                  style={{ border: 'none' }}
                />
              </div>
            </div>
          )}
          {(section === "indian-risk-map-forecast" && subsection === "risk-split") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <div style={{ width: '100%', height: '800px', margin: '2rem 0' }}>
                <iframe
                  src="https://geopulse-dash-backend1.up.railway.app/"
                  title="Dash App"
                  width="100%"
                  height="100%"
                  style={{ border: 'none', minHeight: '800px' }}
                />
              </div>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}

// export async function generateStaticParams() {
//   return [
//     { section: 'poverty-patterns', subsection: 'poverty-maps' },
//     { section: 'poverty-patterns', subsection: 'density-trends' },

//     { section: 'malnutrition-development', subsection: 'health-indicators' },
//     { section: 'malnutrition-development', subsection: 'data-segmentation' },

//     { section: 'urbanization-migration', subsection: 'migration-analysis' },
//     { section: 'urbanization-migration', subsection: 'skill-shortage-identification' },

//     { section: 'economic-forces-and-currency-depreciation', subsection: 'currency-analysis' },
//     { section: 'economic-forces-and-currency-depreciation', subsection: 'economic-stress' },
//     { section: 'economic-forces-and-currency-depreciation', subsection: 'regional-comparison' },
//     { section: 'economic-forces-and-currency-depreciation', subsection: 'regional-comparison1' },

//     { section: 'predictive-risk-map', subsection: 'composite-risk' },
//     { section: 'predictive-risk-map', subsection: 'future-risk-zones' }
//   ];
// }

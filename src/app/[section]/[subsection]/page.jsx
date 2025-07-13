import { notFound } from 'next/navigation';
import Link from 'next/link';
import { navConfig } from '@/config/nav';
import { Card, CardContent } from '@/components/ui/card';
import { Home, ChevronRight } from 'lucide-react';
import Plot4_1 from '@/components/4.1plot';
import Plot3_1 from '@/components/3.1plot';
import Plot3_2 from '@/components/3.2plot';
import Plot1_1 from '@/components/1.1plot';
import Plot1_2 from '@/components/1.2plot';
import Plot2_1 from '@/components/2.1plot';
import Plot2_2 from '@/components/2.2plot';

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
          {(section === "population-density-vs-poverty" && subsection === "poverty-maps") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot1_1 />
            </div>
          )}
          {(section === "population-density-vs-poverty" && subsection === "density-trends") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot1_2 />
            </div>
          )}
          {(section === "malnutrition-development" && subsection === "health-indicators") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot2_1 />
            </div>
          )}
          {(section === "malnutrition-development" && subsection === "data-segmentation") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot2_2 />
            </div>
          )}
          {(section === "urbanization-migration" && subsection === "migration-analysis") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot3_1 />
            </div>
          )}
          {(section === "urbanization-migration" && subsection === "skill-shortage-identification") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot3_2 />
            </div>
          )}
          {(section === "inr-depreciation" && subsection === "currency-analysis") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <Plot4_1 />
            </div>
          )}
          {(section === "predictive-risk-map" && subsection === "composite-risk") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <div style={{ width: '100%', height: '800px', margin: '2rem 0' }}>
                <iframe
                  src="http://localhost:8051/"
                  title="Dash App"
                  width="100%"
                  height="100%"
                  style={{ border: 'none' }}
                />
              </div>
            </div>
          )}
          {(section === "predictive-risk-map" && subsection === "future-risk-zones") && (
            <div className="bg-muted rounded-lg w-full overflow-hidden">
              <div style={{ width: '100%', height: '800px', margin: '2rem 0' }}>
                <iframe
                  src="http://localhost:8052/"
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

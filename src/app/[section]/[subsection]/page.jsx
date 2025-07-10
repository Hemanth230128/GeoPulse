import { notFound } from 'next/navigation';
import Link from 'next/link';
import { navConfig } from '@/config/nav';
import { Card, CardContent } from '@/components/ui/card';
import { Home, ChevronRight } from 'lucide-react';

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
          <h1 className="text-3xl font-bold mb-1">{title}</h1>
          <p className="text-muted-foreground mb-6">Content for this page will be determined later.</p>
          
          <p className="mb-2">This is the dedicated page for {sectionTitle}, {title}.</p>
          <p className="mb-8">Further details and components for this subsection will be implemented in the future.</p>

          <div className="bg-muted rounded-lg h-80 flex items-center justify-center">
            <p className="text-muted-foreground">Placeholder Content Area</p>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

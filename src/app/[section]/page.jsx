import Link from 'next/link';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Home, ChevronRight } from 'lucide-react';

function unslugify(slug) {
  return slug.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

export default function SectionPage({ params }) {
  const { section } = params;
  
  const title = unslugify(section);

  return (
    <div>
      <div className="flex items-center space-x-2 text-sm text-muted-foreground mb-4">
        <Link href="/" className="hover:text-foreground">
          <Home className="h-4 w-4" />
        </Link>
        <ChevronRight className="h-4 w-4" />
        <span className="font-medium text-foreground">{title}</span>
      </div>
      <Card className="shadow-lg">
        <CardHeader>
          <CardTitle className="text-3xl">Welcome to {title}</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-muted-foreground">
            Please select a subsection from the sidebar to view more details. This is the main page for the '{title}' section.
          </p>
        </CardContent>
      </Card>
    </div>
  );
}

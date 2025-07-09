import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

function unslugify(slug) {
  return slug.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

export default function SectionPage({ params }) {
  const { section } = params;
  
  const title = unslugify(section);

  return (
    <Card className="shadow-md">
      <CardHeader>
        <CardTitle className="text-3xl">Welcome to {title}</CardTitle>
      </CardHeader>
      <CardContent>
        <p className="text-muted-foreground">
          Please select a subsection from the sidebar to view more details. This is the main page for the '{title}' section.
        </p>
      </CardContent>
    </Card>
  );
}

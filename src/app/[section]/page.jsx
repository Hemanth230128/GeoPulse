import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

export default function SectionPage({ params }) {
  const { section } = params;
  
  const title = section.charAt(0).toUpperCase() + section.slice(1);

  return (
    <Card className="shadow-md">
      <CardHeader>
        <CardTitle className="font-headline text-3xl">Welcome to {title}</CardTitle>
      </CardHeader>
      <CardContent>
        <p className="text-muted-foreground">
          Please select a subsection from the sidebar to view more details. This is the main page for the '{title}' section.
        </p>
      </CardContent>
    </Card>
  );
}

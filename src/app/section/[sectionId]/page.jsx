import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { ArrowLeft } from 'lucide-react';
import { getSectionData } from '@/lib/sections';

export default function SectionPage({ params }) {
  const section = getSectionData(params.sectionId);
  const sectionTitle = section ? section.title : `Section ${params.sectionId}`;

  return (
    <div className="flex items-center justify-center min-h-[calc(100vh-200px)]">
        <Card className="w-full max-w-md">
            <CardHeader>
                <CardTitle className="text-3xl font-bold">{sectionTitle}</CardTitle>
                <CardDescription>
                    Welcome to {sectionTitle}.
                </CardDescription>
            </CardHeader>
            <CardContent>
                <div className="flex items-center gap-2 text-muted-foreground">
                    <ArrowLeft className="h-5 w-5 animate-pulse" />
                    <p>Please select a subsection from the sidebar to view its content.</p>
                </div>
            </CardContent>
        </Card>
    </div>
  );
}

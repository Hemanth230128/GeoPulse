import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { ArrowLeft } from 'lucide-react';

export default function SectionPage({ params }: { params: { sectionId: string } }) {
  return (
    <div className="flex items-center justify-center min-h-[calc(100vh-200px)]">
        <Card className="w-full max-w-md">
            <CardHeader>
                <CardTitle className="text-3xl font-bold">Section {params.sectionId}</CardTitle>
                <CardDescription>
                    Welcome to Section {params.sectionId}.
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

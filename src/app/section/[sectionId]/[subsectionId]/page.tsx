import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { ChevronRight } from 'lucide-react';

export default function SubsectionPage({ params }: { params: { sectionId: string; subsectionId: string } }) {
  const subsectionNameMap: { [key: string]: string } = {
    a: 'A',
    b: 'B',
    c: 'C',
  };

  return (
    <div>
        <div className="flex items-center gap-2 mb-4 text-sm text-muted-foreground">
            <span>Section {params.sectionId}</span>
            <ChevronRight className="h-4 w-4" />
            <span className="text-primary font-medium">Subsection {subsectionNameMap[params.subsectionId]}</span>
        </div>
        <Card>
            <CardHeader>
                <CardTitle className="text-3xl font-bold">
                    Subsection {subsectionNameMap[params.subsectionId]}
                </CardTitle>
                <CardDescription>
                    Content for this page will be determined later.
                </CardDescription>
            </CardHeader>
            <CardContent>
                <div className="space-y-4">
                    <p>This is the dedicated page for Section {params.sectionId}, Subsection {subsectionNameMap[params.subsectionId]}.</p>
                    <p>Further details and components for this subsection will be implemented in the future.</p>
                    <div className="aspect-video bg-secondary rounded-lg flex items-center justify-center">
                        <p className="text-muted-foreground">Placeholder Content Area</p>
                    </div>
                </div>
            </CardContent>
        </Card>
    </div>
  );
}

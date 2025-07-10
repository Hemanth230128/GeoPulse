import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { ChevronRight } from 'lucide-react';
import { getSectionData, getSubsectionData } from '@/lib/sections';
import WorldHeatmap from '@/components/WorldHeatmap';

export default function SubsectionPage({ params }: { params: { sectionId: string; subsectionId: string } }) {
    const section = getSectionData(params.sectionId);
    const subsection = getSubsectionData(params.sectionId, params.subsectionId);

    const sectionTitle = section ? section.title : `Section ${params.sectionId}`;
    const subsectionTitle = subsection ? subsection.name : `Subsection ${params.subsectionId}`;

    return (
        <div>
            <div className="flex items-center gap-2 mb-4 text-sm text-muted-foreground">
                <span>{sectionTitle}</span>
                <ChevronRight className="h-4 w-4" />
                <span className="text-primary font-medium">{subsectionTitle}</span>
            </div>
            <Card>
                <CardHeader>
                    <CardTitle className="text-3xl font-bold">
                        {subsectionTitle}
                    </CardTitle>
                    <CardDescription>
                        Content for this page will be determined later.
                    </CardDescription>
                </CardHeader>
                <CardContent>
                    <div className="space-y-4">
                        <p>This is the dedicated page for {sectionTitle}, {subsectionTitle}.</p>
                        <p>Further details and components for this subsection will be implemented in the future.</p>
                        <div className="aspect-video bg-secondary rounded-lg flex items-center justify-center">
                            <WorldHeatmap />
                        </div>
                    </div>
                </CardContent>
            </Card>
        </div>
    );
}

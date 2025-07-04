import Link from 'next/link';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { ArrowRight } from 'lucide-react';

const sections = Array.from({ length: 5 }, (_, i) => ({
  id: i + 1,
  title: `Section ${i + 1}`,
  description: `Explore the features of Section ${i + 1}.`,
  href: `/section/${i + 1}`,
}));

export default function Home() {
  return (
    <div className="flex flex-1 flex-col items-center justify-center p-4 text-center">
      <div className="mx-auto max-w-4xl">
        <h1 className="text-4xl font-bold tracking-tight text-primary sm:text-5xl md:text-6xl">
          Welcome to Geopulse Navigator
        </h1>
        <p className="mt-6 text-lg leading-8 text-muted-foreground">
          Your central hub for exploring geographical data and insights. Select a section below to begin your journey.
        </p>
      </div>

      <div className="mt-16 grid w-full max-w-5xl gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {sections.map((section) => (
          <Link href={section.href} key={section.id} className="group">
            <Card className="h-full transform transition-transform duration-300 ease-in-out group-hover:-translate-y-1 group-hover:shadow-xl">
              <CardHeader>
                <CardTitle className="flex items-center justify-between">
                  {section.title}
                  <ArrowRight className="h-5 w-5 text-muted-foreground transition-transform duration-300 group-hover:translate-x-1 group-hover:text-accent" />
                </CardTitle>
                <CardDescription>{section.description}</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="h-24 rounded-lg bg-secondary flex items-center justify-center">
                  <span className="text-muted-foreground">Map Preview</span>
                </div>
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}

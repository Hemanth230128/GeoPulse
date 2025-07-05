import Link from 'next/link';
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
  CardDescription,
} from '@/components/ui/card';
import { sections } from '@/lib/sections';

const FeatureCard = ({ feature }) => (
  <Link href={feature.href} key={feature.id} className="group block h-full">
    <Card className="flex h-full flex-col overflow-hidden transition-all duration-300 ease-in-out group-hover:-translate-y-2 group-hover:shadow-xl">
      <CardHeader>
        <CardTitle className="text-xl font-semibold tracking-tight text-primary">
          {feature.title}
        </CardTitle>
        <CardDescription className="pt-2 text-muted-foreground">
          {feature.description}
        </CardDescription>
      </CardHeader>
      <CardContent className="flex flex-1 items-center justify-center p-6">
        <feature.Icon className="h-20 w-20 text-muted-foreground/50 transition-all group-hover:scale-110 group-hover:text-muted-foreground" />
      </CardContent>
    </Card>
  </Link>
);

export default function Home() {
  return (
    <div className="flex-1 bg-background">
      <div className="container mx-auto flex h-full max-w-7xl flex-col justify-center px-4 py-12 sm:px-6 lg:px-8">
        <div className="text-center">
          <h1 className="font-headline text-4xl font-bold tracking-tighter text-primary sm:text-5xl md:text-6xl">
            GeoPulse
          </h1>
          <p className="mx-auto mt-4 max-w-[700px] text-lg text-muted-foreground md:text-xl">
            Actionable insights for a world on the pulse.
          </p>
        </div>
        <div className="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {sections.map((feature) => (
            <FeatureCard key={feature.id} feature={feature} />
          ))}
        </div>
      </div>
    </div>
  );
}

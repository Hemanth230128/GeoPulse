import Link from 'next/link';
import {
  Card,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { sections, type Section } from '@/lib/sections';

const FeatureCard = ({
  feature,
}: {
  feature: Section;
}) => (
  <Link href={feature.href} key={feature.id} className="group block h-full">
    <Card className="flex h-full flex-col justify-center overflow-hidden transition-all duration-300 ease-in-out group-hover:-translate-y-2 group-hover:shadow-2xl">
      <CardHeader>
        <CardTitle className="flex items-center gap-3 text-lg font-semibold tracking-tight text-primary">
          <feature.Icon className="h-8 w-8 shrink-0" />
          <span className="flex-1">{feature.title}</span>
        </CardTitle>
        <CardDescription className="pt-2 text-sm text-muted-foreground">
          {feature.description}
        </CardDescription>
      </CardHeader>
    </Card>
  </Link>
);

export default function Home() {
  return (
    <div className="flex flex-1 flex-col items-center justify-center bg-background">
      <div className="container mx-auto w-full max-w-6xl px-4 text-center sm:px-6 lg:px-8">
        <h1 className="font-headline text-4xl font-bold tracking-tighter text-primary sm:text-5xl md:text-6xl">
          GeoPulse
        </h1>
        <p className="mx-auto mt-4 max-w-[700px] text-lg text-muted-foreground md:text-xl">
          Actionable insights on impulse, feel the world&apos;s true pulse.
        </p>
        <div className="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-5">
          {sections.map((feature) => (
            <FeatureCard key={feature.id} feature={feature} />
          ))}
        </div>
      </div>
    </div>
  );
}
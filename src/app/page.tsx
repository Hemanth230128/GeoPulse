import Link from 'next/link';
import Image from 'next/image';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { cn } from '@/lib/utils';

const features = [
  {
    id: 1,
    title: 'Global Terrain Analysis',
    description: 'High-resolution topographical data for strategic planning.',
    href: '/section/1',
    aiHint: 'terrain map',
    imgSrc: 'https://placehold.co/600x400.png',
  },
  {
    id: 2,
    title: 'Maritime Route Planning',
    description: 'Optimize sea lanes with real-time oceanographic insights.',
    href: '/section/2',
    aiHint: 'shipping lanes',
    imgSrc: 'https://placehold.co/600x400.png',
  },
  {
    id: 3,
    title: 'Atmospheric Visualization',
    description: 'Track and forecast weather patterns with predictive models.',
    href: '/section/3',
    aiHint: 'weather patterns',
    imgSrc: 'https://placehold.co/600x400.png',
  },
  {
    id: 4,
    title: 'Urban Growth Patterns',
    description: 'Analyze satellite imagery to monitor metropolitan expansion.',
    href: '/section/4',
    aiHint: 'city aerial',
    imgSrc: 'https://placehold.co/600x400.png',
  },
  {
    id: 5,
    title: 'Agricultural Monitoring',
    description: 'Monitor crop health and yield with advanced satellite data.',
    href: '/section/5',
    aiHint: 'farm aerial',
    imgSrc: 'https://placehold.co/600x400.png',
  },
];

const FeatureCard = ({
  feature,
  className,
}: {
  feature: (typeof features)[0];
  className?: string;
}) => (
  <Link href={feature.href} key={feature.id} className={cn('group block', className)}>
    <Card className="h-full overflow-hidden transition-all duration-300 ease-in-out group-hover:-translate-y-2 group-hover:shadow-2xl">
      <CardContent className="p-0">
        <Image
          src={feature.imgSrc}
          alt={feature.title}
          width={600}
          height={400}
          className="aspect-video w-full object-cover"
          data-ai-hint={feature.aiHint}
        />
      </CardContent>
      <CardHeader>
        <CardTitle className="text-xl font-semibold tracking-tight text-primary">
          {feature.title}
        </CardTitle>
        <CardDescription className="text-base text-muted-foreground">
          {feature.description}
        </CardDescription>
      </CardHeader>
    </Card>
  </Link>
);

export default function Home() {
  return (
    <div className="flex flex-1 flex-col bg-background">
      <section className="w-full py-20 md:py-32 lg:py-40">
        <div className="container mx-auto px-4 text-center md:px-6">
          <h1 className="font-headline text-4xl font-bold tracking-tighter text-primary sm:text-5xl md:text-6xl lg:text-7xl">
            GeoPulse
          </h1>
          <p className="mx-auto mt-6 max-w-[700px] text-lg text-muted-foreground md:text-xl">
            Clarity and foresight, feel the world&apos;s true pulse.
          </p>
        </div>
      </section>

      <section className="w-full pb-20 md:pb-32 lg:pb-40">
        <div className="container mx-auto px-4 md:px-6">
          <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
            <FeatureCard feature={features[0]} className="lg:col-span-2" />
            <FeatureCard feature={features[1]} />
            <FeatureCard feature={features[2]} />
            <FeatureCard feature={features[3]} className="lg:col-span-2" />
            <FeatureCard feature={features[4]} className="lg:col-span-2" />
          </div>
        </div>
      </section>
    </div>
  );
}
